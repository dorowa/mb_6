<html>
    <head>
        <title>Добавить альбом</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    </head>
    <body>
        <div class="container">
            <div class="row">
                <div class="col-12 p-2" style="background-color: blue; border-radius: 20px 20px 0 0">
                    <h3 style="text-transform: uppercase; text-align: center; color: yellow; "><a href="/albums/all/" style="text-decoration: none"><-</a>Добавить новый альбом</h3>
                </div>
                <div class="col-12 m-0 p-1" style="background-color: yellow; color: blue; border-radius: 0 0 20px 20px">
                    <form action="/albums/" method="POST" style="display: flex; flex-direction: column; flex-wrap: wrap; align-items: center;">
                        <div class="col-7" style="display: flex; justify-content: space-between;">
                            <label for="in1">Исполнитель:</label>
                            <input name="artist" type="text" id="in1">
                        </div>

                        <div class="col-7" style="display: flex; justify-content: space-between;">
                            <label for="in2">Альбом:</label>
                            <input name="album" type="text" id="in2">
                        </div>
                        
                        <div class="col-7" style="display: flex; justify-content: space-between;">
                            <label for="in3">Год выхода:</label>
                            <input name="year" type="text" id="in3">
                        </div>
                        
                        <div class="col-7" style="display: flex; justify-content: space-between;">
                            <label for="in4">Жанр:</label>
                            <input name="genre" type="text" id="in4">
                        </div>
                        
                        <div class="col-12 p-1" style="text-align: center;"><input value="Добавить" type="submit" /></div>
                    </form>
                </div>
            </div>
        </div>
    </body>
</html>
