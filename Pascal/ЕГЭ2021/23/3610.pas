uses school;
function f(start, endn:integer):integer;
begin
  if start = endn then f:=1
  else if start > endn then f:=0
  else f:=f(start * 2, endn)+f(start * 3, endn)
end;

begin
  Writeln('Ответ: ', f(8, 96) * f(96, 3456))
end.