uses school;
function f(start, cc:integer):sequence of integer;
begin
  if cc < 5 then 
    yield sequence f(start + 2, cc + 1)+
                    f(start + 3, cc + 1)+
                    f(start * 2, cc + 1)
  else if cc = 5 then yield start
end;

begin
  Writeln('Ответ: ', f(10, 0).Distinct.Count)
end.