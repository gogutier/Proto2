from django.contrib import admin
from blog.models import Post, Comment, appointment, ProdID, Book, ProgramaConv, PruebaMod, PruebaTabla, OrdenProg, DetalleProg, ProdReal, Maquinas, Turnos, Minuta, OrderInfo, Padron, DiaConv2, OrdenProgCorr, DetalleProgCorr, Meses, Semanas, FotoInventario, ProyMkt, ProyMktMes, ProyMktPadron, ProdRealCorr, InfoWIP, Camion, OrdenCorrplan, FotoCorrplan, Cartones, CalleBPT, BobInvCic, MovPallets, Pallet, UbicPallet, PalletCic, TomaInvCic, DatosWIP_Prog, FotoProgCorr, IDProgCorr,Datos_Inv_WIP,Foto_Datos_Inv_WIP, Datos_Proy_WIP,Datos_MovPallets, FiltroEntradaWIP, FiltroSalidaWIP, Foto_Calles_Inv_Cic_WIP, Foto_Inv_Cic_WIP, Foto_Palletscti_Inv_Cic_WIP, Foto_Palletsencontrados_Inv_Cic_WIP, Foto_Palletsnoencontrados_Inv_Cic_WIP, Foto_Palletsenotracalle_Inv_Cic_WIP, MovRollos, ConsumoRollos, Foto_ConsumoRollos, Foto_Datos_MovPallets, m2Maqruta_WIP, Datos_MovPallets_B


# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)#Cuando se agregan estos hay que aplicar el migrate

admin.site.register(appointment)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(ProdID)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(Book)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(ProgramaConv)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(PruebaMod)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(PruebaTabla)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(OrdenProg)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(DetalleProg)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(ProdReal)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(Maquinas)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(Turnos)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(Minuta)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(OrderInfo)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(Padron)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(DiaConv2)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(OrdenProgCorr)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(DetalleProgCorr)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(Meses)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(Semanas)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(FotoInventario)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(ProyMkt)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(ProyMktMes)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(ProyMktPadron)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(ProdRealCorr)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(InfoWIP)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(Camion)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(OrdenCorrplan)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(FotoCorrplan)
admin.site.register(Cartones)
admin.site.register(CalleBPT)
admin.site.register(BobInvCic)
admin.site.register(MovPallets)
admin.site.register(Pallet)
admin.site.register(UbicPallet)
admin.site.register(PalletCic)
admin.site.register(TomaInvCic)
admin.site.register(DatosWIP_Prog)
admin.site.register(FotoProgCorr)
admin.site.register(IDProgCorr)
admin.site.register(Datos_Proy_WIP)
admin.site.register(Datos_MovPallets)
admin.site.register(Datos_Inv_WIP)
admin.site.register(Foto_Datos_Inv_WIP)
admin.site.register(FiltroEntradaWIP)
admin.site.register(FiltroSalidaWIP)
admin.site.register(Foto_Calles_Inv_Cic_WIP)
admin.site.register(Foto_Inv_Cic_WIP)
admin.site.register(Foto_Palletscti_Inv_Cic_WIP)
admin.site.register(Foto_Palletsencontrados_Inv_Cic_WIP)
admin.site.register(Foto_Palletsnoencontrados_Inv_Cic_WIP)
admin.site.register(Foto_Palletsenotracalle_Inv_Cic_WIP)
admin.site.register(MovRollos)
admin.site.register(ConsumoRollos)
admin.site.register(Foto_ConsumoRollos)
admin.site.register(Foto_Datos_MovPallets)
admin.site.register(Datos_MovPallets_B)
