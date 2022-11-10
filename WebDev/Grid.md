# Grid
1. Single column

    ```css
    * {
      margin: 0;
      padding: 0;
    }

    .grid {
      display: grid;
    }

    .grid div:nth-child(even) {
      background-color: red;
    }

    .grid div:nth-child(odd) {
      background-color: green;
    }

    ```

    ```html
    <!DOCTYPE html>
    <html>
    <head>
    <title>Grid test</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="style.css">
    <style>
    /*
    style here
    */
    </style>
    </head>
    <body>

    <div class="grid">

        <div class="title">title</div>
        <div class="header">header</div>
        <div class="sidebar">sidebar</div>
        <div class="content">content</div>
        <div class="footer">footer</div>

    </div>


    </body>
    </html>
    ```

    ![grid1.png](:storage\\fb837300-0f6a-4d8d-a8c8-c5b1264621de\\b9623a3e.png)

1. Add column with 
    ```css
    grid-template-columns: 2fr;
    ```

    ![grid2.jpg](:storage\\fb837300-0f6a-4d8d-a8c8-c5b1264621de\\117d2807.jpg)

1. You can have additional columns, defining the width for each one: `
    ```css
    grid-template-columns: 2fr 1fr;
    ```

    ![grid3.png](:storage\\fb837300-0f6a-4d8d-a8c8-c5b1264621de\\22937598.png)
    
    * By `fr`
        ```css
        grid-template-columns: 2fr 1fr;
        ```
    
    * By `%`
        ```css
        grid-template-columns: 20% 1fr;
        ```
    
    * By `px`
        ```css
        grid-template-columns: 20px 1fr;
        ```
    
    * By `auto` : for adapting the column to the content
        ```css
        grid-template-columns: auto 1fr;
        ```


