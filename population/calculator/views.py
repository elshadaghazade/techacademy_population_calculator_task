from django.shortcuts import render
import datetime, math

def homepage(request):

    params = {
        'result': '',
        'error_message': '',
        'year': request.POST.get('year', '').strip()
    }

    if 'year' in request.POST:
        try:
            year = int(params['year'])

            if year < datetime.date.today().year:
                raise Exception("Il kohne ola bilmez")

            # hər 8 saniyədən bir yeni doğuş
            # hər 12 saniyədən bir ölüm
            # hər 29 saniyədən bir yeni immiqrant

            bir_saniyeye_olan_artim = 1/8 - 1/12 + 1/29
            artim = (year - datetime.date.today().year) * 60 * 60 * 24 * 365 * bir_saniyeye_olan_artim

            params['result'] = f"{year}-ci ilde {math.ceil(artim)} qeder insan artacaq"

        except ValueError:
            params['error_message'] = 'Dogru il daxil edin'
        except Exception as err:
            params['error_message'] = str(err)


    return render(request, 'calculator/homepage.html', params)