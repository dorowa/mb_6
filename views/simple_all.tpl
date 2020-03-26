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
                    <h1>{{header}}<a href="/albums/" style="text-decoration: none">+</a></h1>
                </div>
                <div class="col-12 p-1" style="background-color: yellow; text-align: left; border-radius: 0 0 20px 20px;">
                    % for artist in artists:
                        <pre class="h5" style="color: blue; font-weight: 400; wrap-content: wrap">Исполнитель: <strong><a href="/albums/{{artist[0]}}" style="text-decoration: none">{{artist[0]}}</a></strong>, альбомов жанра <i>'{{artist[3]}}'</i> - {{artist[2]}}</pre>
                        % for album in artist[1]:
                            <pre class="ml-2 h6"><strong>{{album[0]}}</strong>, <i>{{album[1]}}</i>, {{album[2]}}</pre>
                        % end
                    <br>
                    % end
                </div>
        </div>
    </body>
</html>
