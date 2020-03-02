#-*- coding: cp936 -*-
try:
    from osgeo import gdal
    from osgeo import ogr
    from osgeo import osr
except ImportError:
    import gdal
    import ogr

def WriteVectorFile():
    # Ϊ��֧������·��������������������
    gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8","NO")
    # Ϊ��ʹ���Ա��ֶ�֧�����ģ��������������
    gdal.SetConfigOption("SHAPE_ENCODING","GB2312")

    strVectorFile ="D:\\GitHub\PyGdalStudy\\GDALShp\\Data\\TestPolygon.shp"

    # ע�����е�����
    ogr.RegisterAll()

    # �������ݣ������Դ���ESRI��shp�ļ�Ϊ��
    strDriverName = "ESRI Shapefile"
    oDriver =ogr.GetDriverByName(strDriverName)
    if oDriver == None:
        print("%s ���������ã�\n", strDriverName)
        return

    # ��������Դ
    oDS =oDriver.CreateDataSource(strVectorFile)
    if oDS == None:
        print("�����ļ���%s��ʧ�ܣ�", strVectorFile)
        return

    #����ͶӰ
    targetSR = osr.SpatialReference()
    targetSR.ImportFromEPSG(4326) #Geo WGS84
    # ����ͼ�㣬����һ�������ͼ�㣬����û��ָ���ռ�ο��������Ҫ�Ļ�����Ҫ���������ָ��
    papszLCO = []
    oLayer =oDS.CreateLayer("TestPolygon", targetSR, ogr.wkbPolygon, papszLCO)
    if oLayer == None:
        print("ͼ�㴴��ʧ�ܣ�\n")
        return

    # ----------------------���洴�����Ա�----------------------------
    # �ȴ���һ����FieldID����������
    oFieldID =ogr.FieldDefn("FieldID", ogr.OFTInteger)
    oLayer.CreateField(oFieldID, 1)

    # �ٴ���һ����FeatureName���ַ������ԣ��ַ�����Ϊ100
    oFieldName =ogr.FieldDefn("FieldName", ogr.OFTString)
    oFieldName.SetWidth(100)
    oLayer.CreateField(oFieldName, 1)

    #--------------------------����Ҫ��--------------------------------
    oDefn = oLayer.GetLayerDefn()

    # ����������Ҫ��
    oFeatureTriangle = ogr.Feature(oDefn)
    #�����ֶ�����ֵ
    oFeatureTriangle.SetField(0, 0)
    oFeatureTriangle.SetField(1, "������")
    #���ռ�Ҫ�ظ������ζ�������ֵ----��������
    geomTriangle =ogr.CreateGeometryFromWkt("POLYGON ((0 0,20 0,10 15,0 0))")
    #��Ҫ�����ü�������
    oFeatureTriangle.SetGeometry(geomTriangle)
    #����Ҫ��
    oLayer.CreateFeature(oFeatureTriangle)

    # ��������Ҫ��
    oFeatureRectangle = ogr.Feature(oDefn)
    oFeatureRectangle.SetField(0, 1)
    oFeatureRectangle.SetField(1, "����")
    geomRectangle =ogr.CreateGeometryFromWkt("POLYGON ((30 0,60 0,60 30,30 30,30 0))")
    oFeatureRectangle.SetGeometry(geomRectangle)
    oLayer.CreateFeature(oFeatureRectangle)

    # ������Ҫ��
    # oFeaturePoint = ogr.Feature(oDefn)
    # oFeaturePoint.SetField(0, 2)
    # oFeaturePoint.SetField(1, "��")
    # #geomPoint =ogr.CreateGeometryFromWkt("Point(10,20)")
    # geomPoint = ogr.Geometry(ogr.wkbPoint)
    # geomPoint.AddPoint(10,20)
    # oFeaturePoint.SetGeometry(geomPoint)
    # oLayer.CreateFeature(oFeaturePoint)

    oDS.Destroy()
    print("���ݼ�������ɣ�\n")

#����
WriteVectorFile()