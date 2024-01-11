from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# 1. 직접 가져오기
# from .models import User
# 위 방법은 권장 하지 않는다.
# 2. settings에 설정된 모델 가져오기
# from django.conf import settings    # model = settings.AUTH_USER_MODEL
# 위 방법은 문자열이기 때문에 models.py에 작성할때 사용하도록
# 3. get_user_model 메서드 활용
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # fields = '__all__'