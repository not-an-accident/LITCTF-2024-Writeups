from Crypto.Util.number import long_to_bytes
from math import gcd
n = 20139389823467560324951007135496663034311406724762925649947463397488857229545044314285031397899829537994825455909177884674408656213020493819112487220585270002430726136383100828599724625502823207778515971391709770854157672070879200655198634784742886978704381272219725533443981315911789543803461093739084283207709450684337279547819258025199962324253575300988984880591756037321233866025114309493453448958479911502088051125641125368151775912177940109708219193295213133759450625394778382993100184093719168739090966942584409963417300430733162478617184899298883994527152984771626591321030825165909828349189439672616578710887
c = 5087763012396498520567000327855429536717492339039737633508362028657687351332971208275497459273466862547681154026872977866360211826128717994416002867751897144680064142658162377763866307064197030325615475506927316680702996654123068622347572452060519133237536269668922875028208294559357025145045711638709550724612613642124525126951578930971043944518804750849917803837633980228312569245801839040579573442318766525792374401937615900638933807200264665541797361075170233281418340784821574360078549932486788115667378813016956259780016911992269098774257603925370047932497170295221576660666022176213366103523968451777351185352
ct_received_2=18582105993084142669782011871535478742263934964467308744301688345409111233906752298286443339896394891463885205071469025696042537352211423246738768726355652134205770962961707963444135955564233553667632698037603676912120356763806472839141529899769731715211311071654868346010347288712016938623054833481453920469350148868471536413295460862985502471701271015843933922253217197322257232156489005370429738561975976729202390282512928488604369560443618138554439656091264997496455874216901522891256983492959083611075683706561324158056476383427719274734779960309937214349007700332967744700071328131467948501495957427883273179969
#Finding p using method described above
p=gcd(ct_received_2-2, n)
#n=pq
q=n//p
#Finding d now that we know phi(n)
phi=(p-1)*(q-1)
d=pow(p, -1, phi)
print(long_to_bytes(pow(c,d,n)))
