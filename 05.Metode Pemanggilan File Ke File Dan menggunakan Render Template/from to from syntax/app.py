# membuat class halo dunia 

class halodunia:
    # membuat function self dengan nilai return format str halo dunia
    def __init__(self):
        # membuat self pada variabel_hasil halo 
        # atau menggunakan syntax html juga bisa 
        self.hasil_halo =  f"""
        <!DOCTYPE html>
        <html>
            <head>
                <title>HALO FILE TO FILE</title>
            </head>
            <body>
                <div>
                    <h1>FILE TO FILE SYNTAX FLASK</h1>
                    <p>
                     file to file 
                    </p>
                    <p>
                    file to file 
                    </p>
                </div>
            </body>
        </html>
        """


    # output 
    def hasil(self):
        # mengirim hasil 
        return self.hasil_halo

