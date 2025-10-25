# vue-tutorial

A crud made with JavaScript.

---

## 步骤 1：最小应用

目标：挂载 Vue 应用，使用 v-cloak 防止闪烁，返回一个 ref 字段给模板显示

关键点：
- `Vue.createApp(...).mount('#app')`
- `setup` 返回响应式数据
- `ref` 适合原始类型

代码文件名：step1.html

---

## 步骤 2：静态列表

目标：用 v-for 渲染数组，理解 :key 的必要性（稳定、唯一，便于高效 diff）

关键点：
- `v-for="h in heroes" :key="h.id"`
- 模板插值 `{{ }}`

代码文件名：step2.html

---

## 步骤 3：受控输入

目标：用 reactive 管理对象表单；用 `:value + @input` 显式同步，不用 v-model，贴近后端“可控”思维

关键点：
- `reactive(createEmptyHero())`
- `onAddNameInput(e) { addForm.name = e.target.value }`
- 受控输入便于校验、调试与测试

代码文件名：step3.html

---

## 步骤 4：纯函数区

目标：将数据处理逻辑抽到“纯函数区”，与 Vue 解耦，便于独立测试和复用

包含：
- `createEmptyHero`
- `prepareHeroName`（裁剪、默认名）
- `prepareHeroHp`（字符串转数值，取整，最小为 0）
- `addHeroToList`（不可变添加，返回新数组与 nextId）

代码文件名：step4.html

---

## 步骤 5：删除功能

目标：实现查找与删除（不可变）

包含：
- `findHeroIndexById`（手写循环）
- `removeHeroFromList`（`slice + splice` 返回新数组）
- 列表中添加“删除”按钮与点击事件

代码文件名：step5.html

---

## 步骤 6：编辑模式切换

目标：进入编辑态并填充 `editForm`，支持取消

包含：
- `editingId: ref(null)`
- `isEditing: computed(() => editingId.value !== null)`（本教程用普通函数）
- `startEditing`：根据 id 找到英雄，设置 `editingId` 并填充 `editForm`
- `cancelEditing`：重置 `editingId` 与 `editForm`

代码文件名：step6.html

---

## 步骤 7：更新功能

目标：提交编辑并不可变更新列表

包含：
- `updateHeroInList`：通过索引 `splice(idx, 1, updated)`
- 提交前校验 `editForm.id` 与 `editingId` 合法
- 提交后调用 `cancelEditing` 复位状态

代码文件名：step7.html

---

## 步骤 8：完整功能整合

目标：合并新增、编辑、删除，计算 `nextId` 初始值，得到完整功能版本

包含：
- 初始 `heroes`
- 初始 `nextId`：扫描现有 heroes 的最大 id
- 新增（受控输入 + 纯函数）/ 编辑（填充、提交）/ 删除（不可变）

代码文件名：step8.html

---

## 进阶

- v-model 对比：将受控输入改为 `v-model` 版本，体会两者差异与取舍
- 持久化：用 `localStorage` 保存 `heroes`，在 `mounted` 或 `setup` 初期加载，`watch` 变化后写入
- 组件化：将列表区和表单区拆为子组件，用 props/emit 通信，保持“纯函数区”不变
