# payment/views.py
import json
from json import JSONDecodeError
import requests

from django.db.models import F
from django.http import (HttpResponse, JsonResponse,
                         HttpResponseBadRequest, HttpResponseRedirect)
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# from django.views import View

from order.models import Order
# from menu.models import MenuModel
# from order.models import OrderMoldel
# from payment.models import PaymentModel
# from restaurant.models import RestaurantModel
# from server.collection import convert_body_to_data  ### 얘도 추상화 잘 해서 코드 줄일 방법좀...
menus={'1':'아메리카노', '2': '카페라떼','23':'초코쉐이크'}
headers = {
    'Authorization': "KakaoAK 71af8dbb8f935a60b315cede1dec6368",
    'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
}

pay_url = 'https://kapi.kakao.com/v1/payment/ready'
check_url = 'https://kapi.kakao.com/v1/payment/approve'

fail_url = 'http://172.30.1.53:8000/menu/'
cancel_rul = 'http://172.30.1.53:8000/order/'


@csrf_exempt
def Pay(request):
    thisorder = Order.objects.get(is_paid=False, user=request.user)
    idx=[]
    idx = thisorder.order.split(",")
    restaurant_name=menus[idx[0]]
    total_cost = thisorder.price
    # Should make response page urls
    approval_url = 'http://172.30.1.53:8000/check/'

    # Body
    body = {
        'cid': 'TC0ONETIME',
        'partner_order_id': 'partner_order_id',
        'partner_user_id': 'partner_user_id',
        'item_name': restaurant_name,
        'quantity': 1,
        'total_amount': total_cost,
        'vat_amount': total_cost // 10,
        'tax_free_amount': 0,
        'approval_url': approval_url,
        'fail_url': fail_url,
        'cancel_url': cancel_rul
    }

    # Get response
    res = requests.post(url=pay_url, headers=headers, data=body)
    req_data = json.loads(res.text)
    try:
        tid = req_data['tid']
        redirection_url = req_data['next_redirect_mobile_url']
    except KeyError as err:
        return JsonResponse(req_data)

    thisorder.tid = tid
    thisorder.save()

    return HttpResponseRedirect(redirection_url)


# csrf, POST만
def Check(request):
    thisorder = Order.objects.get(user=request.user)
    total_cost = thisorder.price
    tid = thisorder.tid
    pg_token = request.GET['pg_token']

    body = {
        'cid': 'TC0ONETIME',
        'tid': tid,
        'partner_order_id': 'partner_order_id',
        'partner_user_id': 'partner_user_id',
        'pg_token': pg_token,
        'total_amount': total_cost
    }

    res = requests.post(url=check_url, headers=headers, data=body)
    approve_data = json.loads(res.text)
    thisorder.is_paid = True
    return JsonResponse(approve_data)
