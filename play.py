B
    �|=][  �               @   s�  d dl Z d dlZd dlZd dlZd dlZd dlZedd�Ze�	e�Z
e
d Ze
d Ze
d Ze
d Zdeef Zd	d
ee� ddddddde de dd�Zd	ddddde de dd�Zdd� Zdd� Zdd� Zdd� Zdd� Zy�eee� ej�d �d!k�rNe�d"� ej�d#�d!k�r:e�d$� e�  eeee� ne�  eeee� nVe�d%� e�d"� ej�d#�d!k�r�e�d$� e�  eeee� ne�  eeee� W n( ek
�r�   ed&� e�d'� Y nX dS )(�    Nzcfg.json�rZmember_tokenZ	device_idZcookie_cfduidZcookie_PHPSESSIDzmember_token=%s&device_id=%sztzz.tahuweb.comz%sz.application/json, text/javascript, */*; q=0.01zfile://z�Mozilla/5.0 (Linux; Android 8.1.0; vivo 1814 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36z0application/x-www-form-urlencoded; charset=UTF-8Zdeflatezid-ID,en-US;q=0.9z__cfduid=%szPHPSESSID=%szcom.news.tahuweb)�Hostzcontent-length�accept�originz
user-agentzcontent-typezaccept-encodingzaccept-language�cookier   zx-requested-with)r   r   z
user-agentzaccept-encodingzaccept-languager   r   zx-requested-withc             C   s�   t �d� tjd| |d�}|�� }td� td|d d  � td|d d	  � td
|d d  � td|d d  � td|d d  � td� d S )N�clearz&https://tzz.tahuweb.com/User/User/user)�url�headers�dataz�[34m
		
.-----. .--.  .-. .-..-. .-. 
`-' '-'/ {} \ { {_} || } { | 
  } { /  /\  \| { } }\ `-' / 
  `-' `-'  `-'`-' `-' `---'  
                             z[32mUsername[31m: [33m%s�user�member_namez[32mPhone   [31m: [33m%sZmember_phonez[32mGold    [31m: [33m%sZmember_goldz[32mBalance [31m: [33m%sZmember_incomez[32mBonus   [31m: [33m%sZmember_bonusz"[1;30m
Bot Berjalan....... [37m
)�os�system�requestsZpost�json�print)�hr
   �a�b� r   �line.py�Uinfo   s    
r   c             C   s�   d| }t j|| d�}|j}t�d|�}t|�}|�dd�}t�d|�}t|�}	|	�dd�}
|
�dd	�}|�d
d�}|�dd�}|�dd	�}tdd�}|�|� |�	�  d S )NzThttps://tzz.tahuweb.com/Content/Category/chose_category?lang=indonesian&device_id=%s)r   r	   zdata-value='{(.*?)}�\� z"category_id":(.*?),�[�]�
�'� �,z
cookie.dat�w)
r   �get�text�re�findall�str�replace�open�write�close)�h2�deviceZu_idx�idx�iZresZaswZres2Zres3ZrewZrew2Zrew3Zrew4Zrew5Zrew6Zrew7r   r   r   �Cid1   s     

r.   c             C   s�   d|||f }t j|| d�}|j}t�d|�}t|�}|�dd�}	|	�dd�}
|
�dd�}|�d	d�}|�d
d�}tdd�}|�|� |�	�  d S )Nzohttps://tzz.tahuweb.com/Content/Content/content_list?lang=indonesian&cid=%s&page=1&member_token=%s&device_id=%s)r   r	   z*'Content','Win.pageParam.content_id=(.*?);r   r   r   r   r   r   r   zcookies.datza+)
r   r!   r"   r#   r$   r%   r&   r'   r(   r)   )r*   �tokenr+   �cidZu_listZcgetZcgettZcgerZfkZfk1Zfk2Zfk3Zfk4Zfk5Ztulr   r   r   �ClistB   s    

r1   c              C   s�   t j�d�dkrPt �d� ttt� tdd��� } xP| D ]}t	tt
t|� q8W n4ttt� tdd��� }x|D ]}t	tt
t|� qnW d S )Nz../cookie.datTzrm -f cookie.datz
cookie.datr   )r   �path�existsr   r.   r*   r+   r'   �	readlinesr1   r/   )Zhior0   Zhoir   r   r   �CoidP   s    




r5   c             C   sj   t dd��� }xV|D ]N}d| ||f }tj||d�}|jdkrRtd� t�d� qtd� t�	�  qW d S )	Nzcookies.datr   zghttps://tzz.tahuweb.com/Content/Content/read?member_token=%s&content_id=%s&lang=indonesian&device_id=%s)r   r	   ��   z([32mSuccess membaca artikel[31m. [37m�   z[31mGagal membaca [37m
)
r'   r4   r   r!   Zstatus_coder   �timeZsleep�sys�exit)r/   r+   r*   ZfakZcontenZu_bacaZgbacar   r   r   �baca\   s    

r;   z	./cookiesTZcookieszcookies.datzrm -f cookies.datzmkdir cookiesz [31m
Program berhenti!!! [37m
�   )r   r#   r   �os.pathr   r9   r8   r'   Zfil�loadZcfgr/   r+   ZcfduidZsessidr
   �lenr   r*   r   r.   r1   r5   r;   r2   r3   �chdirr   �KeyboardInterruptr   r:   r   r   r   r   �<module>   sh   0








