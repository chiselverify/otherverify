-- Code your design here
library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity accualu is
  port (
  	clock: in std_logic;
    reset: in std_logic;
  	op: in std_logic_vector(2 downto 0);
    din: in std_logic_vector(31 downto 0);
    enable: in std_logic;
    accu: out std_logic_vector(31 downto 0)
    );
end entity;
    
architecture beh of accualu is

signal accuReg: signed(31 downto 0);
signal res: signed(31 downto 0);
signal a, b: signed(31 downto 0);

begin

a <= signed(accuReg);
b <= signed(din);

--ALU Logic
process(all) begin
	case (op) is
	 when 3d"0" => res <= a; --NOP
    when 3d"1" => res <= a + b; -- ADD
    when 3d"2" => res <= a - b; -- SUB
    when 3d"3" => res <= a and b;--AND
    when 3d"4"  => res <= a or b;--OR
    when 3d"5" => res <= a XOR b;--XOR
    when 3d"6" => res <= b;--      LD
    when 3d"7" => res <= '0' & a(31 downto 1); --SHR
    when others => res <= a;
    end case;
  end process;

--Output register
process(all) begin
if rising_edge(clock) then
	if (reset='1') then
    	accuReg <= (others => '0');
    elsif (enable='1') then
    	accuReg <= res;
  	end if;
end if;
end process;

accu <= std_logic_vector(accuReg);

end beh;