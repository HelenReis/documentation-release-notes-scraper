class PostTemplate:
    def get_template(self):
        return [
            '---', 
            " title: version", 
            " date: 'date_now'", 
            " description: Notas de versão version",
            " thumbnailUrl: '/javascript-functions-thumbnail.jpeg'",
            " tags: ['version', 'javascript']",
            " ---",
            "",
            " <div>",
            "body_version",
            " </div>"]