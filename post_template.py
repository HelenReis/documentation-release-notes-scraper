class PostTemplate:
    def get_template(self):
        return [
            '---', 
            " title: title_version", 
            " date: 'date_now'", 
            " description: Notas de versão version",
            " thumbnailUrl: '/javascript-functions-thumbnail.jpeg'",
            " tags: ['title_version']",
            " ---",
            "",
            " <div>",
            "body_version",
            " </div>"]