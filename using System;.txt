using System;
using System.IO.Ports;
using UnityEngine;

public class Flex3CubeScale : MonoBehaviour
{
    public string portName = "COM8";   // change if needed

    public Transform cube1;
    public Transform cube2;
    public Transform cube3;

    public float minSize = 1f;
    public float maxSize = 3f;

    SerialPort sp;

    void Start()
    {
        sp = new SerialPort(portName, 115200);
        sp.ReadTimeout = 100;
        sp.Open();
        Debug.Log("Serial Connected");
    }

    void Update()
    {
        if (sp == null || !sp.IsOpen) return;

        try
        {
            string line = sp.ReadLine();
            string[] values = line.Split(',');

            if (values.Length != 3) return;

            float v1 = Mathf.Clamp01(float.Parse(values[0]));
            float v2 = Mathf.Clamp01(float.Parse(values[1]));
            float v3 = Mathf.Clamp01(float.Parse(values[2]));

            cube1.localScale = Vector3.one * Mathf.Lerp(minSize, maxSize, v1);
            cube2.localScale = Vector3.one * Mathf.Lerp(minSize, maxSize, v2);
            cube3.localScale = Vector3.one * Mathf.Lerp(minSize, maxSize, v3);
        }
        catch { }
    }

    void OnDestroy()
    {
        if (sp != null && sp.IsOpen)
            sp.Close();
    }
}
