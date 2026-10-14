def department_summary(employees):
    summary = {}
    for emp in employees:
        dept = emp["department"]
        sal = emp["salary"]

        if dept not in summary:
            summary[dept]={
                "headcount":0,
                "total_salary":0
            }
        summary[dept]["headcount"]+=1
        summary[dept]["Total_salary"]+=sal
    for dept in summary:
        count = summary[dept]["headcount"]
        total = summary[dept]["total_salary"]

        summary[dept]["avg-sal"]=total/count
        del summary[dept]["total_salary"]
        
    return summary