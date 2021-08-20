odoo.define("my_library.counter", function (require) {
  const AbstractAction = require("web.AbstractAction");
  const core = require("web.core");

  const OurAction = AbstractAction.extend({
    template: "my_library.ClientAction",
    info: "this message comes from the JS",
    start: function () {
      // this.$el.html("hello");
    },
  });

  core.action_registry.add("my_library.action", OurAction);
});
