# fetch_chartink.py
import requests

def fetch_chartink_data():
    url = "https://chartink.com/screener/process"

    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://chartink.com",
        "referer": "https://chartink.com/screener/supertrend-2023-12-19-8",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
        "x-csrf-token": "27av7sv94zLzj6F9CReGrXq5SINpcRaSxqmtCEbc",  # Update this frequently
        "x-requested-with": "XMLHttpRequest",
        "cookie": "_ga=GA1.2.1093095750.1752066522; _cc_id=ac479c7ac7f52758d39f25b9e56f3c46; _gid=GA1.2.1023231993.1752656377; __gads=ID=66e894583e7db13b:T=1752066529:RT=1752658991:S=ALNI_MZZJIrqtceJrBzn2UxZ_zHmQqkzMg; __gpi=UID=00001158a41bd3f1:T=1752066529:RT=1752658991:S=ALNI_MYrPQ_u8u5e1zeXfkscJk7a5KSlpQ; __eoi=ID=ca85a738bf7274e0:T=1752066529:RT=1752658991:S=AA-AfjZ-3SsgAsxqbsnLFjLj_gR3; __utma=102564947.1093095750.1752066522.1752659007.1752659007.1; __utmc=102564947; __utmz=102564947.1752659007.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=102564947.1.10.1752659007; panoramaId_expiry=1752745419038; panoramaId=b5502a490707ad9b9d5900ee9e1ba9fb927a07b7958f59291b75f6af45360d26; panoramaIdType=panoDevice; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6Im1SVm1SUldHQjJla1ExZndIa3IzN0E9PSIsInZhbHVlIjoiUXo5ZEJCRGNwMjE4TVN3ZkV0VFk0R3FpZWhUTnhLdVhLT3ZNelZNL3gzY3ZGeVVjVE5kWC9uZm5kTW9pVjBiQUNzNGJJRkxRT0xyL29TSjNPUFh4UzBha2dSd21haXlpbnVvVXBScjZvYWF5YmJQNUJsQjZyNGdsY0laUGN3elhvaUdJVDBrdG00b1hTa3BDZHZGbWExRnI2bHBOTWdZV0FuYUc0K0NEVmIyWkVOTHFmYzhlYWJ3VmlmOUhZcWgwd0ZYK1UwZ2xQLzhBYVlsRUNNbDRPRDVlWUhiZ0IzcGcvb2NqTFRwUWZnQT0iLCJtYWMiOiIzOWQyZDZhZDRmNDM1YmFjZmFiZTZjZjhjNjFiMTdmM2NjNTA3OTRkNmY5YzBjNDFlZGY2NTM5YzBmM2UzODNmIiwidGFnIjoiIn0%3D; FCNEC=%5B%5B%22AKsRol_r9-No3u7kjeeXP3a4JtUtrVt0cbFtjT-CvksJCTE5DzZYlyu2HgdzzY6kW9i-ENsvagI2ZX-5FSAWK221w4xFVCU6gL8glE4fPm8BzVVAcMQ3YdznjhzBNZIK_xj0TXdZdlnoJuUtVG3KqDjMXdmOw1q5yA%3D%3D%22%5D%5D; _ga_7P3KPC3ZPP=GS2.2.s1752658991$o8$g1$t1752659047$j4$l0$h0; XSRF-TOKEN=eyJpdiI6IlZnVmlQQmI5eVpkVktKT2FDQXdrUmc9PSIsInZhbHVlIjoiZnEzOEsyaEpOMUc4LzBNNWtJODdCVTVZQW16RGhKeW93UzBESms3ZTZ3TlRVclV4VDhXM21xRlVXNUhuREF0YTVuVU9Udm9CdzdIdGFCQzZKSmlpZkpGdGZmY0RRTmN6elRqKzFXWkd2a25yU01SVCt4ZXM2VWUwVlNBZWxlNzMiLCJtYWMiOiJmYWYyODFmNGYwZDcxMWU3ZjUzMjIwNTViYmEzMjEyODYzMGVjMzg0Y2M5OTU0MGE2MTlhYzgyMDg2NzMyNjAwIiwidGFnIjoiIn0%3D; ci_session=eyJpdiI6InlDTk10Wkh1eW1FekRZcVhtQURjM0E9PSIsInZhbHVlIjoiYW1tUDBzcksvS0N0RTdZbEJ0bHNFM0hyN1pCZjlJTFZBK3RXQ21VNFpBNjBDQWVjT0dzZVBpdnovd2IvVW40c3lPWVkyMzZGYlNqK2JOZ04rbVRycW9iYklqSGR4bDhQRkRYNzUxMzZaWkVFbUNucFR5Vi9CNExMY0p0MTl0NlMiLCJtYWMiOiJhOWVhYmIwNjFlMDlkODQ2Y2JjZjUxNWIzNDExZmI4NDg5YjMwMTZhYjM4YjhkNDRjZTJjODc2MDM4ZmQwN2IyIiwidGFnIjoiIn0%3D"
  
    }

    body = "scan_clause=(+%7Bcash%7D+(+market+cap+%3E+5000+and+1+day+ago+close+%3C+1+day+ago+supertrend(+7+%2C+3+)+and+%5B0%5D+1+hour+close+%3E+latest+supertrend(+7+%2C+3+)+and+earning+per+share%5Beps%5D+%3E+0.1+)+)+&debug_clause=groupcount(+1+where+market+cap+%3E+5000)%2Cgroupcount(+1+where+1+day+ago+close+%3C+1+day+ago+supertrend(+7+%2C+3+))%2Cgroupcount(+1+where+%5B0%5D+1+hour+close+%3E+daily+supertrend(+7+%2C+3+))%2Cgroupcount(+1+where+earning+per+share%5Beps%5D+%3E+0.1)"

    try:
        response = requests.post(url, headers=headers, data=body)
        response.raise_for_status()
        result = response.json()
        data = result.get("data", [])
        print("nsecode(s):", end=" ")
        for item in data:
            print(item.get("nsecode", ""), end=" ")
        print()
    except Exception as e:
        print("Error fetching Chartink data:", e)

if __name__ == "__main__":
    fetch_chartink_data()
