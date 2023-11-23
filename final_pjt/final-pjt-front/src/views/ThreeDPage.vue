<template>
  <div>
    <!-- 3D 애니메이션을 표시할 컨테이너 -->
    <div ref="canvasContainer" class="3d"></div>

    <!-- 확인 버튼 -->
    
    <router-link :to="{ name: 'main' }">메인 페이지로 이동</router-link>
  </div>
</template>

<script>
import * as THREE from 'three';

export default {
  mounted() {
    // Three.js를 사용하여 3D 애니메이션을 생성하는 코드 작성
    // 예시로 기본적인 씬을 만들고 렌더러를 추가하는 코드를 작성할 수 있습니다.
    // 이 부분은 Three.js 사용법에 따라 작성되어야 합니다.
    // https://threejs.org/docs/

    // 예시: 빨간색 큐브 생성
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    this.$refs.canvasContainer.appendChild(renderer.domElement);

    const geometry = new THREE.BoxGeometry();
    const material = new THREE.MeshBasicMaterial({ color: 0xff0000 });
    const cube = new THREE.Mesh(geometry, material);
    scene.add(cube);

    camera.position.z = 5;

    const animate = function () {
      requestAnimationFrame(animate);

      cube.rotation.x += 0.01;
      cube.rotation.y += 0.01;

      renderer.render(scene, camera);
    };

    animate();
  },
  methods: {
    goToMainPage() {
      // 메인 페이지로 이동하는 코드
      this.$router.push({ path: '/main' });
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