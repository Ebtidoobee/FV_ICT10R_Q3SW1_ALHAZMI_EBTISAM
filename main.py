from js import document

def check_eligibility(registered, medical, grade):
    if not registered or registered == "no":
        return "❌ Please complete the online registration.", ""
    if not medical or medical == "no":
        return "❌ Please secure a medical clearance.", ""
    
    try:
        grade_num = int(grade)
    except:
        return "❌ Please select your Grade level.", ""

    teams = {
        7: ("Blue Bears", "https://via.placeholder.com/150/0000FF/FFFFFF?text=Blue+Bears"),
        8: ("Red Bulldogs", "https://via.placeholder.com/150/FF0000/FFFFFF?text=Red+Bulldogs"),
        9: ("Yellow Tigers", "https://via.placeholder.com/150/FFD700/000000?text=Yellow+Tigers"),
        10: ("Green Hornets", "https://via.placeholder.com/150/008000/FFFFFF?text=Green+Hornets")
    }
    
    if grade_num in teams:
        team_name, img_src = teams[grade_num]
        return f"🎉 Congratulations!<br>You are part of the <strong>{team_name}</strong>!", img_src
    else:
        return "❌ Only Grades 7–10 are allowed.", ""

def check_eligibility_py(event):
    reg = None
    med = None
    
    # Get values from Radio Buttons
    for r in document.getElementsByName("register"):
        if r.checked:
            reg = r.value
            break
    for m in document.getElementsByName("medical"):
        if m.checked:
            med = m.value
            break
            
    grade = document.getElementById("grade").value

    result_text, img_src = check_eligibility(reg, med, grade)
    
    # Update result
    result_div = document.getElementById("result")
    result_div.innerHTML = result_text

    team_img = document.getElementById("teamImage")
    if img_src:
        team_img.src = img_src
        team_img.style.display = "block"
    else:
        team_img.style.display = "none"
