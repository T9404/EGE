uses school;
function f(start, endn:integer):integer;
begin
  if start = endn then f:=1
  else if start < endn then f:=0
  else f:=f(start - 1, endn)+f(start div 2, endn)
end;

begin
  Writeln('Ответ: ', f(Dec('110111', 2),6))
end.