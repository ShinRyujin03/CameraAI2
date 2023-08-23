import os
class Config:
    img_path = "/Users/macbookairm1/Desktop/K-Pop/IU/pic/IU.PNG"
    img_name = os.path.basename(img_path)
    # host and port
    host = '0.0.0.0'
    port = 1102

    #database
    db_host ='localhost'
    db_user = 'root'
    db_password = ''
    db_name = "face_metadata" 