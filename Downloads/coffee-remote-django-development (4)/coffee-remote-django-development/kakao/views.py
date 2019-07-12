from order.models import Order
from order.serializers import OrderSerializer
from rest_framework import viewsets
from django.shortcuts import render
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter



# #토큰을 얻을 코드 구하기 - 카카오측에서 아래 함수로 redirect해줌.
# def oauthCode(request):
#     context = {
#         'code': ''
#     }
#     return render(request, 'order/kakao.html', context)
#
# #리다이렉트되어 code를 얻어옴. 이를 통해 토큰을 발급받고 해당 유저 확인.
# def oauthCodeCallback(request):
#     #발급받은 code 얻어오고 이를 통해 토큰을 발급받기.
#     code = request.GET.get('code')
#     url = "https://kauth.kakao.com/oauth/token"
#     payload = "grant_type=authorization_code&" \
#               "client_id=e9324bb26945caf079b1b63862ff7347&" \
#               "redirect_uri=http://localhost:8000/accounts/kakao/login/callback/&" \
#               "code=" + code
#     headers = {
#         'Content-Type': "application/x-www-form-urlencoded",
#         'Cache-Control': "no-cache",
#     }
#     response = requests.request("POST", url, data=payload, headers=headers)
#     #토큰을 얻어옴.
#     tokens = json.loads((response.text).encode('utf-8'))
#     access_token = json.loads((response.text).encode('utf-8'))['access_token']
#     print(tokens)
#
#     # #해당 토큰을 통해 유저 정보 확인해보기.
#     # url = "https://kapi.kakao.com/v2/user/me"
#     # headers = {
#     #     'Content-Type': "application/x-www-form-urlencoded",
#     #     'Cache-Control': "no-cache",
#     #     'Authorization': "Bearer " + access_token
#     # }
#     # response = requests.request("POST", url, headers=headers)
#     # print(response.text)
#
#     context = {
#         'code': access_token
#     }
#     return render(request, 'order/kakao.html', context)
#
# def oauthLogOut(request):
#     access_token = request.POST.get('access_token')
#     url = "https://kapi.kakao.com/v1/user/logout"
#     headers = {
#         'Authorization': "Bearer " + access_token
#     }
#     response = requests.request("POST", url, headers=headers)
#     print(response.text)
#     id = json.loads((response.text).encode('utf-8'))['id']
#
#     context = {
#         'code': id
#     }
#     return render(request,'order/kakao.html', context)
#     return HttpResponse(status=204)
#
# def oauthCheck(request):
#     access_token = request.POST.get('access_token')
#     url = "https://kauth.kakao.com/v1/user/access_token_info"
#     headers = {
#         'Authorization': "Bearer " + access_token
#     }
#     response = requests.request("POST", url, headers=headers)
#     print(response.text)
#     expiresInMillis = json.loads((response.text).encode('utf-8'))['expiresInMillis']
#
#     context = {
#         'code': expiresInMillis
#     }
#     response = requests.request("POST", url, data=payload, headers=headers)