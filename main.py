import camera
IP_WEB_CAM_URL = 'https://192.168.185.239:8080/video'
camera.capture(IP_WEB_CAM_URL)
camera.destroy()