try:
    import urllib2 as Ulib
except :
    import urllib.request as Ulib
import json

Slack_Url = "https://hooks.slack.com/services/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"

def send(data):
    # data: dict()
    req = Ulib.Request(Slack_Url)
    # endata = urllib.urlencode(data)
    req.add_header('Content-type', "application/json")
    endata = json.dumps(data).encode('utf-8')
    response = Ulib.urlopen(req, endata).read()
    print(response)
    if response == 'ok' or response == b'ok':
        return
    else:
        send(data)

def generate_slack_data(content, color="good"):
    # change content to slace data fomart
    slack_data_format = {
        "attachments": [{
            # "fallback": fallback,
            "color": color,
            # "pretext": "Optional text that appears above the attachment block",
            # "title": title,
            # "title_link": title_link,
            "text": content,
            # "fields": [
            #     {
            #         "title": "Priority",
            #         "value": "High",
            #         "short": false
            #     }
            # ],
            # "image_url": image,
            # "thumb_url": "http://example.com/path/to/thumb.png",
            "footer": "US LA",
            # "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
            # "ts": 123456789
        }]
    }
    # data = slack_data_format.update()
    return slack_data_format
