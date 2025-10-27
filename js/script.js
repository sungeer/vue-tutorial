<script>
    (function () {
        var reactive = Vue.reactive;  // 用于对象、数组的响应式
        var ref = Vue.ref;

        function createEmptyHero() {
            return { id: 0, name: '', hp: '' };
        }

        var app = Vue.createApp({
            setup: function () {
                var title = ref('英雄管理面板（步骤3）');
                var addForm = reactive(createEmptyHero());  // 将一个对象变成响应式对象

                function onAddNameInput(e) {
                    addForm.name = e.target.value;
                }

                function onAddHpInput(e) {
                    addForm.hp = e.target.value;
                }

                return {
                    title: title,
                    addForm: addForm,
                    onAddNameInput: onAddNameInput,
                    onAddHpInput: onAddHpInput
                };
            }
        });

        app.mount('#app');
    })();
</script>