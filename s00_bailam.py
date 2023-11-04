#region debai
"""
--- ma debai / id
get_name_in_email(email_list)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/toya03emailhople

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo trinhduyetweb de kiemtra tep s00_bailam.py, va lay diachi/url aka githubbailamurl

02b dán diachi githubbailamurl theo mẫu ở trang web duoiday
    https://forms.gle/ZwjSxkx9mEqhL8mj6

--- debai / problem
Viết hàm 
  get_name_in_email(email_list)
trả về tên tài khoản trong email 
Nếu email không hợp lệ, trả về 'ERROR invaid email'

--- vidu mau / testcase
Khi chay voi input                                        | Ketqua output
--------------------------------------------------------- | -----------------
get_name_in_email(['ai-btx@gmail.com'])                   | ['ai-btx']
get_name_in_email(['user1@gmail.com', 'user2@gmail.com']) | ['user1', 'user2']
get_name_in_email([])                                     | []
get_name_in_email(['abb#ccc'])                            | ['ERROR invaid email']
get_name_in_email([None])                                 | ['ERROR invaid email']
get_name_in_email([None, 'abb#ccc'])                      | ['ERROR invaid email', 'ERROR invaid email']
"""
#endregion debai

#region bailam
def get_name_in_email(email_list):
  text=''
  x=[]
  a=[]
  if not email_list:
    x[0:1]=[]
    return x[0:1]
  if len(email_list)>1:
    x=[]
    for i in range(len(email_list)):
      text = email_list[i]
      if text is not None and text!='' and '@' in text : 
        x= text.split("@")
        a.append(x[0])
      else:
        a.append('ERROR invaid email')
    return a
  elif len(email_list)==1:
    text = email_list[0]
    if text is not None and text!='' and '@' in text : 
      x= text.split("@")
      return x[0:1]
    else:
      x[0:1]=['ERROR invaid email']
      return x[0:1]
  

if __name__=='__main__':
  pass
#endregion bailam
