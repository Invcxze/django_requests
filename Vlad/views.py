from django.http import HttpResponse
def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    remote_addr = request.META["REMOTE_ADDR"]
    return HttpResponse(f"""
      <p> Host: {host} </p>
      <p> User_agent: {user_agent} </p>
      <p> IP ADDR_user : {remote_addr} </p>
    """)
def user(request,name = 'ghost' , post_cloud = 'no-post',num_post='0' ):
    return HttpResponse(f"""\
        <p>user = {name}</p>
        <p>post_cloud = {post_cloud}</p>
        <p>num_post = {num_post}</p>
    """)
def error(request):
    return HttpResponse(f"""
    <h1>К сожалению произошла ошибка </h1>
    """, status = 400, reason = 'Incorrect data')
