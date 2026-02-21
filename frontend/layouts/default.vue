<template>
  <div class="layout">
    <SideMenu />
    <main class="main">
      <slot />
    </main>
  </div>
</template>

<style lang="scss" scoped>
.layout {
  min-height: 100vh;
  width: 100%;
  display: flex;
}

.main {
  flex: 1;
  min-width: 0;
  margin-left: 56px;
  min-height: 100vh;
}
</style>
