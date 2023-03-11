def is_prime(number): # checks to see if the inputed number is prime
    for i in range(2, int(number / 2) + 1):
        if (number % i) == 0:
            return False
    return True

def find_pq(n): # since n is chosen to be the multiplication of two prime numbers (p and q), this method loops through factoring n until we find the two prime nubmers
    for i in range(100): # the two ranges are of 100 based on the fact that n (5561) is less than 100 * 100. Theoretically this could end up not returning the values of p and q, such as with n being 7063 (p = 7, q = 1009), but we could then amend the issue by adjusting the values of the ranges and run the method again
        for j in range(100):
            if is_prime(i) & is_prime(j) & ((i * j) == n): # if both numbers are prime, and if the multiplication of both are equal to the value of n
                print("Values of p and q: ", i, j)

# The below was taken from a stackoverflow post: https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
# and equates to finding d in the "e * d = 1 mod (p - 1) (q - 1)"

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b //a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('DNE')
    else:
        return x % m

encrypted_message = [
    1516, 3860, 2891, 570, 3483, 4022, 3437, 299,
    570, 843, 3433, 5450, 653, 570, 3860, 482,
    3860, 4851, 570, 2187, 4022, 3075, 653, 3860,
    570, 3433, 1511, 2442, 4851, 570, 2187, 3860,
    570, 3433, 1511, 4022, 3411, 5139, 1511, 3433,
    4180, 570, 4169, 4022, 3411, 3075, 570, 3000,
    2442, 2458, 4759, 570, 2863, 2458, 3455, 1106,
    3860, 299, 570, 1511, 3433, 3433, 3000, 653,
    3269, 4951, 4951, 2187, 2187, 2187, 299, 653,
    1106, 1511, 4851, 3860, 3455, 3860, 3075, 299,
    1106, 4022, 3194, 4951, 3437, 2458, 4022, 5139,
    4951, 2442, 3075, 1106, 1511, 3455, 482, 3860,
    653, 4951, 2875, 3668, 2875, 2875, 4951, 3668,
    4063, 4951, 2442, 3455, 3075, 3433, 2442, 5139,
    653, 5077, 2442, 3075, 3860, 5077, 3411, 653,
    3860, 1165, 5077, 2713, 4022, 3075, 5077, 653,
    3433, 2442, 2458, 3409, 3455, 4851, 5139, 5077,
    2713, 2442, 3075, 5077, 3194, 4022, 3075, 3860,
    5077, 3433, 1511, 2442, 4851, 5077, 3000, 3075,
    3860, 482, 3455, 4022, 3411, 653, 2458, 2891,
    5077, 3075, 3860, 3000, 4022, 3075, 3433, 3860,
    1165, 299, 1511, 3433, 3194, 2458
]

# message = ''
# for encrypted_char in encrypted_message: # loops through each individual character in the encoded message
#     message += chr((encrypted_char**(d)) % n) # concatenates each decoded character to the message string. Each character is decoded by exponentiating each block of code the power of the public key and then to the power of the private key mod n; in other words, we use the following formula: M = M^(ed) mod n. Therefore, since we have intercepted the message after being encoded with M^(Alice's key), by encoding this already encoded message with Bob's private key, we are able to find the original message.

# print(message)

# ed = 1mod(p-1)(q-1)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b //a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('DNE')
    else:
        return x % m

n = 3683619794619045316515364657782481231078900881546357936267830272301861025645070737644176180125270180959020129491760228089645272821535330329467299931917931186684564707656486579154771147365705157504754044873740904515593148509272052374272346763171974258241455229386852122892437485353227735143321207985502605074010799365116928319450714910101789324802554840905236193331747783930165331571652250138701223018071931265159861491662820784615346784530477602577043149752746742301014017308845828056809494536349595439566294724766082538248484372168934550697973157064238542368553905472158552871305940181642970221500189562756364976607427748510768106778740758164629386256433316472578200502153507459444778926391863346810567794106361075394445292280199630540472964502747288034212857592709825733164084737619171744769220320182674280233420372837661832518432216772394923204980500189441929611549398448116643436975653489701874457146768222840026547564521
e = 65537
p = 1979028542728256409257043143088178455762334236223249341574423016119745060953784438569471974870646860766210501001140759524650510070835347237716201873807586710776806169880374929742623161187026856783535956701121867059190356999808818768056505740120998878221860166955829588830462447850332911716938166590888885161112293617926918842963800696515739439699763804331001729193491433626929668094945464743565852890835394095929939311244372312773274301215899125722993277823889103
q = 1861327269964922922490369480735026793702562638167770161687514966965972372344804850277925659954742212310954739537663692636073521528901126403649869841640037843758316024457308449548133549359695538297299740504328840890580258893745790036463291641924653334431764099420363651653015879031189463589982100676028540027274885677455359615341487613121077135137298105799290643787530737189074081629650304277247661255303082368957697241448720375301534716296641645897888143950193607
d = 2111742669082078086985958551010049320732798038063661962304021410205734479675770216580394941231465065059605189208156057334880488047635746155735171364909724165203255880363181977591649095589924904597572580678873300937719916728593928311545941075104662173373662426160694281233376089265699059112710699379332565958705154995602607899203241068212373570992825242651488914958986465508647659680463657017580048674977196538799779606989392857451259502900568747523110428908257132775461028207199077358444082420061129173051936941867841524486348838568584975555417217731723579819583963262267371202614757282175210957061391920558447403045844782340084304723771696781709854282822688727180918642566199977523994877752434551317765563806259217759851565624046601374367006174459552656240746254194105768130895843103986215950337905072672264207955983988724650801318905172326605687576246877839735612964023174707378875115230993224278320121334487879926452911869

test_int = modinv(d, (p-1)*(q-1))
print(test_int)