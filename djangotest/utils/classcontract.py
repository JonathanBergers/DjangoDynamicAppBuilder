


def getForms(path):
    from django import forms
    from django.forms import Form

    formObjects = {"text": forms.CharField, "email": forms.EmailField, "date": forms.DateField}

    with open(path, 'r') as myfile:
        data=myfile.read().replace('\n', '')
    import xmltodict
    parsed = xmltodict.parse(data)
    htmlObects = (parsed["form"])["htmlObject"]
    parsedForms = {}
    parameters  =[]
    for i in htmlObects:
        # get form type
        if i["@type"] == "input":
            try:
                inputType = i["inputType"]
                form = formObjects[inputType]

                # try:
                #     length = i["maxLength"]
                # except KeyError:
                #     print("no max length defined, np")


                try:
                    label = i["label"]
                except KeyError:
                    label = "form"
                finally:
                    print(label)
                    parsedForms[label] = form()
            except KeyError:
                print("invalid inputType")

        # Check if max length is defined



    print("parsedforms : " , parsedForms)
    formclass = type("DynamicForm", (Form,), parsedForms)
    print(formclass)
    print(formclass.__dict__)

    return formclass



