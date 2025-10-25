# vue-tutorial

面向 JS 初学者、偏好 Vue 3 组合式与渐进式开发、不喜欢箭头函数的同学。本教程以“英雄管理面板”为目标，从零到一拆解成 8 个小步骤，每步提供完整可运行的 HTML 代码，强调“纯函数区 + 不可变数据更新 + 受控表单”的后端友好思路。

- 框架：Vue 3（CDN 方式）
- 风格：不用箭头函数、显式事件处理、受控输入（不用 v-model）
- 思想：UI 层与领域逻辑解耦（纯函数可独立测试）、不可变列表更新

---

## 目录

- [学习路径总览](#学习路径总览)
- [开始前准备](#开始前准备)
- [步骤 1：最小应用](#步骤-1最小应用)
- [步骤 2：静态列表](#步骤-2静态列表)
- [步骤 3：受控输入](#步骤-3受控输入)
- [步骤 4：纯函数区](#步骤-4纯函数区)
- [步骤 5：删除功能](#步骤-5删除功能)
- [步骤 6：编辑模式切换](#步骤-6编辑模式切换)
- [步骤 7：更新功能](#步骤-7更新功能)
- [步骤 8：完整功能整合](#步骤-8完整功能整合)
- [进阶建议](#进阶建议)
- [常见坑与解法](#常见坑与解法)
- [许可](#许可)

---

## 学习路径总览

1. 搭好最小 Vue3 应用与 v-cloak。
2. 用 v-for 渲染静态列表，理解 :key。
3. 受控表单输入：ref、reactive、:value、@input。
4. 抽出“纯函数区”，与 Vue 解耦。
5. 删除功能：find + 不可变删除。
6. 编辑流程：isEditing、editingId、editForm。
7. 更新功能：不可变替换 + 数据准备（裁剪、转数值）。
8. 合并所有功能（新增、编辑、删除、nextId 计算）。

每一步都是“完整 HTML”，直接复制到本地 .html 文件即可运行。

---

## 开始前准备

- 任意文本编辑器与浏览器（无需构建工具）。
- 每一步代码都包含：
  - `<script src="https://unpkg.com/vue@3/dist/vue.global.prod.js"></script>`
  - `Vue.createApp({ setup: function () { /*...*/ } })`
  - 返回到模板的数据与方法。

建议做法：按步骤创建 8 个文件，如 step1.html ~ step8.html，逐步观察页面行为。

---

## 步骤 1：最小应用

目标：挂载 Vue 应用，使用 v-cloak 防止闪烁，返回一个 ref 字段给模板显示。

关键点：
- `Vue.createApp(...).mount('#app')`
- `setup` 返回响应式数据
- `ref` 适合原始类型

代码文件名建议：step1.html

（从教程中复制“步骤1：最小应用”的完整 HTML 代码）

---

## 步骤 2：静态列表

目标：用 v-for 渲染数组，理解 :key 的必要性（稳定、唯一，便于高效 diff）。

关键点：
- `v-for="h in heroes" :key="h.id"`
- 模板插值 `{{ }}`

代码文件名建议：step2.html

（从教程中复制“步骤2：静态列表”的完整 HTML 代码）

---

## 步骤 3：受控输入

目标：用 reactive 管理对象表单；用 `:value + @input` 显式同步，不用 v-model，贴近后端“可控”思维。

关键点：
- `reactive(createEmptyHero())`
- `onAddNameInput(e) { addForm.name = e.target.value }`
- 受控输入便于校验、调试与测试

代码文件名建议：step3.html

（从教程中复制“步骤3：受控输入”的完整 HTML 代码）

---

## 步骤 4：纯函数区

目标：将数据处理逻辑抽到“纯函数区”，与 Vue 解耦，便于独立测试和复用。

包含：
- `createEmptyHero`
- `prepareHeroName`（裁剪、默认名）
- `prepareHeroHp`（字符串转数值，取整，最小为 0）
- `addHeroToList`（不可变添加，返回新数组与 nextId）

代码文件名建议：step4.html

（从教程中复制“步骤4：纯函数区”的完整 HTML 代码）

---

## 步骤 5：删除功能

目标：实现查找与删除（不可变）。

包含：
- `findHeroIndexById`（手写循环）
- `removeHeroFromList`（`slice + splice` 返回新数组）
- 列表中添加“删除”按钮与点击事件

代码文件名建议：step5.html

（从教程中复制“步骤5：删除功能”的完整 HTML 代码）

---

## 步骤 6：编辑模式切换

目标：进入编辑态并填充 `editForm`，支持取消。

包含：
- `editingId: ref(null)`
- `isEditing: computed(() => editingId.value !== null)`（本教程用普通函数）
- `startEditing`：根据 id 找到英雄，设置 `editingId` 并填充 `editForm`
- `cancelEditing`：重置 `editingId` 与 `editForm`

代码文件名建议：step6.html

（从教程中复制“步骤6：编辑模式切换”的完整 HTML 代码）

---

## 步骤 7：更新功能

目标：提交编辑并不可变更新列表。

包含：
- `updateHeroInList`：通过索引 `splice(idx, 1, updated)`
- 提交前校验 `editForm.id` 与 `editingId` 合法
- 提交后调用 `cancelEditing` 复位状态

代码文件名建议：step7.html

（从教程中复制“步骤7：更新功能”的完整 HTML 代码）

---

## 步骤 8：完整功能整合

目标：合并新增、编辑、删除，计算 `nextId` 初始值，得到完整功能版本。

包含：
- 初始 `heroes`
- 初始 `nextId`：扫描现有 heroes 的最大 id
- 新增（受控输入 + 纯函数）/ 编辑（填充、提交）/ 删除（不可变）

代码文件名建议：step8.html

（从教程中复制“步骤8：完整功能”的完整 HTML 代码）

提示：若想获得更精美的视觉样式，可把 step8 的样式替换为你原始示例的 CSS，即可呈现最终效果。

---

## 进阶建议

- v-model 对比：将受控输入改为 `v-model` 版本，体会两者差异与取舍。
- 纯函数单元测试：用任意测试框架或 `console.assert` 对 `prepareHeroName/prepareHeroHp`、`add/update/remove` 做断言。
- 扩展字段：为英雄增加“阵营/攻击力/法力”等字段，遵循同样的受控与准备流程。
- 表单校验：限制名称长度、HP 上限，禁用“增加/确认修改”按钮并展示错误提示。
- 持久化：用 `localStorage` 保存 `heroes`，在 `mounted` 或 `setup` 初期加载，`watch` 变化后写入。
- 组件化：将列表区和表单区拆为子组件，用 props/emit 通信，保持“纯函数区”不变。

---

## 常见坑与解法

- 数字输入是字符串：`input[type="number"]` 的值也是字符串，统一走 `prepareHeroHp` 转数值取整。
- 不可变更新很关键：避免直接 `heroes.value.push(...)` 或直接改元素；请返回新数组（`slice + push/splice`），利于调试和状态追踪。
- :key 必须稳定且唯一：用 `id`，不要用索引。
- 编辑表单 hp 用字符串：保持输入控件状态一致，提交时再转数值。
- 计算 nextId：初始时扫描现有 `heroes` 的最大 id，新增时 `nextId + 1`。

---

## 许可

- 教程与示例代码可自由学习与修改，用于个人或教学用途无任何限制。若需在生产中使用，请根据你公司的规范进行必要的代码审查和测试。

—

需要我把 8 个步骤的完整 HTML 源码打包为章节点导航的单页演示，或在每一步都套用你原始的高级样式吗？告诉我你的偏好即可。
