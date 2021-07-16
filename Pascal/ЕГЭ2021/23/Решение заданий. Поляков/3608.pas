function getPrime(x:integer):integer;
begin
  var prime := true;
  var n := x + 1;
  for var i := 2 to n div 2 +1 do
  begin
    if n mod i = 0 then
      begin
      prime := false;
      break
      end;
  end;
  if prime then result := n
  else result := getPrime(n)
end;

function f(start, endn:integer):integer;
begin
  if start = endn then f:=1
  else if (start > endn) or (start = 33) then f:=0
  else f:=f(start + 2, endn)+f(getPrime(start), endn)
end;

begin
  Writeln('Ответ: ', f(2, 14) * f(14, 45))
end.