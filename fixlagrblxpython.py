def FPSBooster():
    decalsyeeted = True
    g = game
    w = g.Workspace
    l = g.Lighting
    t = w.Terrain
    l.set_hidden_property("Technology", 2)
    t.set_hidden_property("Decoration", False)
    t.WaterWaveSize = 0
    t.WaterWaveSpeed = 0
    t.WaterReflectance = 0
    t.WaterTransparency = 0
    l.GlobalShadows = False
    l.FogEnd = 9e9
    l.Brightness = 0
    settings().Rendering.QualityLevel = "Level01"
    for i, v in enumerate(g.get_descendants(), start=1):
        if v.is_a("Part") or v.is_a("Union") or v.is_a("CornerWedgePart") or v.is_a("TrussPart"):
            v.Material = "Plastic"
            v.Reflectance = 0
        elif (v.is_a("Decal") or v.is_a("Texture")) and decalsyeeted:
            v.Transparency = 1
        elif v.is_a("ParticleEmitter") or v.is_a("Trail"):
            v.Lifetime = NumberRange(0)
        elif v.is_a("Explosion"):
            v.BlastPressure = 1
            v.BlastRadius = 1
        elif v.is_a("Fire") or v.is_a("SpotLight") or v.is_a("Smoke") or v.is_a("Sparkles"):
            v.Enabled = False
        elif v.is_a("MeshPart"):
            v.Material = "Plastic"
            v.Reflectance = 0
            v.TextureID = 10385902758728957
    for i, e in enumerate(l.get_children(), start=1):
        if e.is_a("BlurEffect") or e.is_a("SunRaysEffect") or e.is_a("ColorCorrectionEffect") or e.is_a("BloomEffect") or e.is_a("DepthOfFieldEffect"):
            e.Enabled = False
FPSBooster()
