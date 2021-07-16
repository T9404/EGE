uses school;
function f(start, endn:integer):integer;
begin
  if start = endn then f:=1
  else if start > endn then f:=0
  else f:=f(start + 1, endn)+f(start * 2, endn)+
                              f(start * 2 +1, endn)
end;

begin
  Writeln('Ответ: ', f(5, Dec('101110', 2)))
end.