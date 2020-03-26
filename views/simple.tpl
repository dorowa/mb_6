<html>
    <head>
        <meta charset="utf-8">
        <title>{{title}}</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    </head>
    <body>
        <div class="container">
            <div class="row">
                <div class="col-12" style="background-color: blue; color: yellow; text-align: center; border-radius: 20px 20px 0 0;">
                    <h1><a href="/albums/all/" style="text-decoration: none"><-</a>{{header}}</h1>
                </div>
                <div class="col-12 p-1" style="background-color: yellow; color: blue; text-align: left; border-radius: 0 0 20px 20px;">
                    <pre class="h6" style="color: black">Всего альбомов у исполнителя: {{count}}</pre>
                    % for content in contents:
                        <h5>{{content[0]}}</h5>
                        <pre class="ml-2 h6">жанр: <strong>{{content[1]}}</strong></pre>
                        <pre class="ml-2 h6">год выпуска: <strong>{{content[2]}}</strong></pre>
                    % end
                </div>
        </div>
    </body>
</html>
