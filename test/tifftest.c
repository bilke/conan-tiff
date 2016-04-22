#include "tiffio.h"
main()
{
    TIFF* tif = TIFFOpen("foo.tif", "w");
    TIFFClose(tif);
}
