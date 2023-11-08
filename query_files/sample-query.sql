select id, name, email, created_at
  from users 
 where email not like '%benchprep%' 
 order by created_at limit 10
;
