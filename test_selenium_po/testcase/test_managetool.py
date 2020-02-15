from test_selenium_po.page.manageTools import ManageTool


class TestManagetool:
    def setup(self):
        self.managetool = ManageTool(reuse=True)

    def test_add_material_pic(self):
        pic_path = 'D:\\Program\\PycharmFile\\practice_11\\test_up.jpg'
        self.managetool.add_material_pic(pic_path)

