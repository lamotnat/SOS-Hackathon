def json_to_string(s):

    words = []

    while len(s) > 1:
        start = s.index(">")
        if start + 1 >= len(s):
            break
        s = s[start+1:]
        end = s.index("<")

        word = s[:end]
        s = s[end:]

        if word == "" or word == " " or len(word)>50:
            continue
    
        if word in words:
            break

        words.append(word)

    s = ""
    for word in words:
        s = s + word
    
    print(s)
    return s
    
    
json_to_string("<s_rvlcdip> ROAD</s_nm><sep/><s_nm> WORK</s_nm><s_price> AHEAD</s_nm><s_price> ROAD</s_nm><s_price> WORK</s_nm><s_price> WORK</s_nm><s_price> AHEAD</s_nm><s_price>")
json_to_string("<s_rvlcdip> <Unakarakarakarakarakarakarakarakarakarakarakarakarakarakaramamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamamama<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOP<s_menu><s_nm> STOPA<s_menu><s_nm> STOPA<s_menu><s_nm> STOPA</s_total>")
json_to_string("<s_rvlcdip> FIRE</s_nm><sep/><s_nm> DEPARTMENT</s_nm><s_price> CONNECTION</s_nm><s_price> ---</s_price><sep/><s_nm>")