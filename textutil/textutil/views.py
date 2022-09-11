from django.http import HttpResponse
from django.shortcuts import render


def home(request):

    return render(request, 'index.html')
    # return HttpResponse("Home")


def analyzer(request):

    # get text from text area (index.html)
    text = request.POST.get('text', "default")

# check boxes(on / off)
    rm_punc = request.POST.get('rmpunc', 'off')  # remove punctuation
    upper = request.POST.get('uppercase', 'off')  # uppercase checkbox
    char_count = request.POST.get('charcount', 'off')  # character count checkbox
    rm_newline = request.POST.get('rmnewline', 'off')  # newline remove
    rm_space = request.POST.get('rmspace', 'off')  # remove extra spaces

# working of checkbox
    if rm_punc == 'on':
        punctions = """{}[]!-_,.#@%$^&*+=/\<>()`~?'\":;"""

        analyzed_text = ''
        for char in text:
            if char not in punctions:  # removes punctions
                analyzed_text += char
        text = analyzed_text

        # para = {'purpose': "Removed Punctuations", "text": analyzed_text}
        # return render(request, 'analyze.html', para)

    if upper == "on":
        analyzed_text = ''
        for char in text:
            analyzed_text += char.upper()  # Converts text to uppercase
        text = analyzed_text

    if rm_newline == 'on':
        # analyzed_text = ''
        analyzed_text = ' '.join(text.splitlines())
        text = analyzed_text

    if rm_space == 'on':
        analyzed_text = ''
        for index, char in enumerate(text):
            if not (text[index] == " " and text[index+1] == " "):
                analyzed_text += char
        text = analyzed_text

    if char_count == "on":

        length = len(text)

        para = {"text": text,
            "statement": "Total number of characters : ", "ans": length}
        return render(request, 'analyze.html', para)

    para = {"text": text}
    return render(request, 'analyze.html', para)

    # else:
    #     return HttpResponse('''<title>Error</title>
    #      <h2>Something Went Wrong . . .</h2>''')


# Not used yet.
def capfirst(request):
    return HttpResponse("Capitalize First")


def rm_newline(request):
    return HttpResponse("Remove New Line")


def rm_space(request):
    return HttpResponse("Remove Space")


def char_count(request):
    return HttpResponse("Character Count")

