<template>
  <div>
    <!-- 3D 애니메이션을 표시할 컨테이너 -->
    <div ref="canvasContainer" class="3d" @click="onCubeClick"></div>
  </div>
</template>

<script>
import * as THREE from 'three';

// 이미지를 불러오기 위한 require 함수 대신 import 사용
import whiteTexture from '@/assets/white.png';

export default {
  mounted() {
    // Three.js를 사용하여 3D 애니메이션을 생성하는 코드 작성
    // 예시로 기본적인 씬을 만들고 렌더러를 추가하는 코드를 작성할 수 있습니다.
    // 이 부분은 Three.js 사용법에 따라 작성되어야 합니다.
    // https://threejs.org/docs/

    // 예시: PlaneGeometry에 텍스처를 입히기
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    this.$refs.canvasContainer.appendChild(renderer.domElement);

    // 텍스처 로더 생성
    const textureLoader = new THREE.TextureLoader();
    // 텍스처 로드 (이미지 경로에 맞게 수정)
    const texture = textureLoader.load(whiteTexture);

    // PlaneGeometry를 이용하여 이미지를 나타낼 면 생성
    const geometry = new THREE.PlaneGeometry(5, 5);
    // 텍스처를 적용한 재질 생성
    const material = new THREE.MeshBasicMaterial({ map: texture, side: THREE.DoubleSide });
    const imagePlane = new THREE.Mesh(geometry, material);
    scene.add(imagePlane);

    camera.position.z = 5;

    const animate = function () {
      requestAnimationFrame(animate);

      // 이미지가 회전하도록 설정
      // imagePlane.rotation.x += 0.005;
      imagePlane.rotation.y += 0.01;

      renderer.render(scene, camera);
    };

    setTimeout(() => {
      this.goToMainPage();
    }, 4100);

    animate();
  },
  methods: {
    goToMainPage() {
      // 메인 페이지로 이동하는 코드
      this.$router.push({ path: '/main' });
    },
    onCubeClick() {
      // 이미지를 클릭했을 때 호출되는 메소드
      this.goToMainPage();
    },
  },
  beforeRouteEnter(to, from, next) {
    // ThreeDPage.vue로 이동할 때 네비게이션 바를 감춤
    document.querySelector('.nav-bar').style.display = 'none';
    next();
  },
  beforeRouteLeave(to, from, next) {
    // ThreeDPage.vue에서 다른 페이지로 이동할 때 네비게이션 바를 다시 표시
    document.querySelector('.nav-bar').style.display = 'block';
    next();
  },
};
</script>

<style scoped>
/* 필요한 스타일 작성 */
.nav-bar {
  display: none;
}
</style>