"""Un sir de caractere introdus de tastatura trebuie sa reprezinta numele si prenumele unei persoane, initialele scrise cu majuscule, celelalte caractere fiind litere mici. 
Stabiliti daca sirul dat este un nume corect de persoana"""
s = input ( "Introduceti numele si pronumele dvs:" )
s1 = s . divizat ()
if (( s1 [ 0 ] == s1 [ 0 ]. title ()) și ( s1 [ 1 ]. title () == s1 [ 1 ])) :
    print ( "numele este corect" )
else :
    print ( "numele este gresit" )
