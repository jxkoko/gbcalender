from datetime import datetime,timedelta,timezone
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render


class HomeTemplateView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def today_datetime(request):
    def get_datetime():
        JST = timezone(timedelta(hours=+9), 'JST')
        dt = datetime.now(JST)
        return dt.day

    context = {"togb":june[str(get_datetime())]}
    # 対応するhtmlファイルを指定
    return render(request, 'main/index.html',context)  

def tomorrow_datetime(request):
    def get_datetime(delta):
        JST = timezone(timedelta(hours=+9), 'JST')
        dt = datetime.now(JST) + timedelta(days=delta)
        return dt.day

    context = {"twgb":june[str(get_datetime(1))]}
    # 対応するhtmlファイルを指定
    return render(request, 'main/index.html',context)

june = {
    "1":"資源ごみ・有害ごみ",
    "2":"可燃ごみ",
    "3":"リサイクルプラ",
    "4":"不燃ごみ",
    "5":"可燃ごみ",
    "6":"なし",
    "7":"なし",
    "8":"その他プラ",
    "9":"可燃ごみ",
    "10":"リサイクルプラ",
    "11":"大型ごみ",
    "12":"可燃ごみ",
    "13":"なし",
    "14":"なし",
    "15":"資源ごみ・有害ごみ",
    "16":"可燃ごみ",
    "17":"リサイクルプラ",
    "18":"不燃ごみ",
    "19":"可燃ごみ",
    "20":"なし",
    "21":"なし",
    "22":"その他プラ",
    "23":"可燃ごみ",
    "24":"リサイクルプラ",
    "25":"大型ごみ",
    "26":"可燃ごみ",
    "27":"なし",
    "28":"なし",
    "29":"なし",
    "30":"可燃ごみ"
}