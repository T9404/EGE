uses school;
function f(start, endn:integer):integer;
begin
  if start = endn then f:=1
  else if start > endn then f:=0
  else f:=f(start + 2, endn)+f(start + 3, endn)+
                              f(start * 10 +1, endn)
end;

begin
  Writeln('Ответ: ', f(3, 12) * f(12, 25))
end.