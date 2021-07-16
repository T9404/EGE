uses school;
function f(start, endn:integer):integer;
begin
  var b := '1'+Bin(start);
  if start = endn then f:=1
  else if start > endn then f:=0
  else f:=f(start + 1, endn)+f(Dec(b, 2), endn)
end;

begin
  Write('Ответ: ', f(4, Dec('110001', 2)))
end.