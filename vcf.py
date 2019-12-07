import vobject

vcard = vobject.readOne('con.vcf')
vcard.prettyPrint()