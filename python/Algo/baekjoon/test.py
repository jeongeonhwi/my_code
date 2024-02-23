from stable_diffusion_tf import StableDiffusion
import matplotlib.pyplot as plt

# 모델 초기화
model = StableDiffusion.from_pretrained('CompVis/stable-diffusion-v1-4')

# 이미지 생성을 위한 프롬프트
prompt = "이 사진을 디즈니 스타일의 카툰으로 변환해주세요"

# 이미지 생성
generated_images = model.generate(prompt)

# 생성된 이미지 시각화
plt.imshow(generated_images[0])
plt.show()