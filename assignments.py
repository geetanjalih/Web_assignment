from bottle import route, run, template, get, post, request,delete,put
p_dict={}
p_info=[]


@post('/member_info/') 
def add_patient():
    p_id = request.POST['p_id']
    p_name = request.POST['name']
    p_gender = request.POST['gender']
    p_age = request.POST['age']
    p_address = request.POST['address']
    p_phone = request.POST['phone']
    p_info = ','.join([p_name,p_gender,p_age,p_address,p_phone])
    p_dict.update({p_id:p_info})
    return p_dict

@get('/member_info/<p_id>')
def show_info(p_id):
    return template('<b> {{p_dict[p_id]}}',p_dict=p_dict,p_id=p_id)


@delete('/member_info/<p_id>')
def delete_member(p_id):
    if p_id in p_dict.keys():
        del(p_dict[p_id])
        return p_dict
    else:
        return "There is no record"

@put('/member_info/')
def add_data():
    p_id = request.POST['p_id']
    p_name = request.POST['name']
    p_gender = request.POST['gender']
    p_age = request.POST['age']
    p_address = request.POST['address']
    p_phone = request.POST['phone']
    p_info = ' '.join([p_name,p_gender,p_age,p_address,p_phone])
    p_dict.update({p_id:p_info})
    return p_dict

run(host='localhost',port=8800)
