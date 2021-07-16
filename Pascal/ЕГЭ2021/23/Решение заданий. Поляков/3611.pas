uses school;
function f(start, endn:integer):integer;
begin
  if start = endn then f:=1
  else if (start > endn) or (start = 43) then f:=0
  else f:=f(start + 2, endn)+
          f(start + (start - 1), endn)+
          f(start + (start + 1), endn)
end;

begin
  Writeln('Ответ: ', f(7, 63))
end.