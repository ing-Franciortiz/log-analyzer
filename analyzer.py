
conteo = {}
THRESHOLD = 3
conteo_user = {}

with open('auth.log', 'r', encoding='utf-8') as auth_log:
    for linea in auth_log:
        if "FAILED" in linea:
            ip = linea.split("ip=")[1].split()[0]
            user = linea.split("user=")[1].split()[0]
            conteo[ip] = conteo.get(ip, 0) + 1
            conteo_user[user] = conteo_user.get(user, 0) + 1
        elif "SUCCESS" in linea:
            ip = linea.split("ip=")[1].split()[0]
            user = linea.split("user=")[1].split()[0]
            if conteo.get(ip, 0) > THRESHOLD:
             print(f"ALERT: {ip} logged in successfully after {conteo[ip]} failed attempts")
            
with open('conteo.txt', 'w', encoding='utf-8') as report:
    for ip, ip_count in conteo.items():
        if ip_count > THRESHOLD:
            print(f"IP: {ip}, Count: {ip_count}", file=report)
    for user, user_count in conteo_user.items():
        if user_count > THRESHOLD:
            print(f"User: {user}, Count: {user_count}", file=report)

for user , user_count in conteo_user.items():
    if user_count > THRESHOLD:
        print(f"User: {user} has exceeded the threshold with {user_count} failed attempts.")
        